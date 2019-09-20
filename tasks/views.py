import stripe
from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import generic

from .forms import ArticleForm
from .models import Piece

stripe.api_key = settings.STRIPE_SECRET_KEY

#########################################################################################
# 		Context processor to determine if current user has pending Pieces				#
#########################################################################################

def has_piece(request):
    has_piece = False
    try:
        user = request.user
        piece = Piece.objects.filter(requested_by=user)
        if piece.count() > 0:
            has_piece = True
    except:
        return has_piece
    return has_piece

####################################################################################
#       Define class based view for Articles page, both POST and GET requests      #
####################################################################################

class ArticlesView(generic.DetailView):
    template_name = 'piece/articles.html'

    def get(self, request):
        article_form = ArticleForm()
        articles = Piece.objects.filter(piece_type='article')
        stripe_key = settings.STRIPE_PUBLISHABLE_KEY
        piece_check = has_piece(request)

        cards = [
            {
                'type': 'Bespoke Content',
                'pieces': [
                    {'price': '€150', 'stripe_price': 15000, 'blurb': 'Written content up to 2,000 words. Ideal for blog posts, interviews, product descriptions, team bios, recipes and press releases.', 'title': 'Copywriting and editorial'},
                    {'price': '€250', 'stripe_price': 25000, 'blurb': 'Written content up to 5,000 words or audiovisual content such as product photography (set of five photos), podcasts (up to three hours of edited recording) or videos of up to 5 minutes.', 'title': 'Multimedia content'},
                    {'price': '€500', 'stripe_price': 50000, 'blurb': 'Management of a business’ social media accounts for specific events (ie. festivals, masterclasses, etc.), including consultation, plan and up to 10 hours of on-site work.', 'title': 'Social media takeover'},
                    {'price': 'Email us', 'stripe_price': '', 'blurb': 'From recipe development to marketing strategy and research, let’s talk and develop a bespoke package that suits your company’s content needs.', 'title': 'Bespoke content design'}
                ]
            },
            {
                'type': 'Tastings and Events',
                'pieces': [
                    {'price': '€150', 'stripe_price': 15000, 'blurb': 'From sourcing producers to menu design, let me help you come up and execute a stress-free, memorable event.', 'title': 'Event planning'},
                    {'price': '€250', 'stripe_price': 25000, 'blurb': 'A two-hour long experience tasting five different wines in an intimate setting. Wine and study material included on the price.', 'title': 'Wine tasting for groups (4 to 8)'},
                    {'price': '€500', 'stripe_price': 50000, 'blurb': 'A two-hour long experience tasting five different wines in an intimate setting. Wine and study material included on the price.', 'title': 'Wine tasting for group (8 to 16)'},
                    {'price': 'Email us', 'stripe_price': '', 'blurb': 'Bigger party? Have something special in mind? Let’s talk and develop a bespoke package that suits your needs.', 'title': 'Bespoke event planning or tasting'}
                ]
            }
        ]

        return render(request, self.template_name, {'articles': articles,  
                                                    'article_form': article_form,
                                                    'cards': cards,
                                                    'piece_check': piece_check,
                                                    'stripe_key': stripe_key})
    
    def post(self, request):
        if request.user.is_authenticated:
            article_form = ArticleForm(request.POST)
            
            if article_form.is_valid():
                user = request.user
                subject = request.POST['subject']
                description = request.POST['description']
                piece_type = request.POST['piece_type']
                article = Piece.objects.create(requested_by=user, 
                                                subject=subject, 
                                                description=description,
                                                status='to_do',
                                                piece_type=piece_type,
                                                price_point='email')

                return render(request, 'piece/charge.html')
                
            else:
                messages.error(request, "Unable to submit your article request at this time.")
                return HttpResponseRedirect(self.request.path_info)


####################################################################################
#               Define function based view for Charge page POST request            #
####################################################################################

class ChargeView(generic.DetailView):
    template_name = 'piece/charge.html'

    def get(self, request):
        piece_check = has_piece(request)
        if piece_check:
            return render(request, self.template_name, {'piece_check': piece_check})
        else:
            return redirect('index')

    def post(self, request):
        user = request.user
        subject = request.POST['subject']
        description = request.POST['description']
        piece_type = request.POST['type']
        price_point = request.POST['price']
        charge = stripe.Charge.create(
            amount=request.POST['stripe_price'],
            currency='eur',
            description=request.POST['subject'],
            source=request.POST['stripeToken']
        )
        article = Piece.objects.create(requested_by=user, subject=subject, description=description, status='To do', piece_type=piece_type, price_point=price_point)
        piece_check = has_piece(request)
        return redirect('charge')


####################################################################################
#               Define function based view for Pieces page GET request             #
####################################################################################

class PiecesView(generic.DetailView):
    template_name = 'piece/pieces.html'

    def get(self, request):
        user = request.user
        pieces = Piece.objects.filter(requested_by=user)
        piece_check = has_piece(request)
        return render(request, self.template_name, {'piece_check': piece_check,
                                                    'pieces': pieces})
