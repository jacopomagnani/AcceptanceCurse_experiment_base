from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1


class MyWaitPage1(WaitPage):

    def after_all_players_arrive(self):
        self.group.initialize_group()


class Page1(Page):

    form_model = 'player'
    form_fields = ['choice']

    def before_next_page(self):
        if self.timeout_happened:
            self.player.late = 1
            flip = random.randint(0,1)
            if flip ==0:
                self.player.choice = 0
            else:
                self.player.choice = 1


class MyWaitPage2(WaitPage):

    def after_all_players_arrive(self):
        self.group.get_outcome()


class Page2(Page):
    pass


class FinalPage(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'paying_round': self.session.vars['paying_round'],
            'part1_payoff': self.participant.vars['part1_payoff']
        }


page_sequence = [
    Intro,
    MyWaitPage1,
    Page1,
    MyWaitPage2,
    Page2,
    FinalPage
]
