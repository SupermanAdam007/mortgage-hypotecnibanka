from bs4 import BeautifulSoup
import requests


class MortgageRequest(object):
    def __init__(self, price_realty: int, want_to_loan: int,
                 time_debit: int, fixed_interest: int = 5):
        self._url = 'https://www.hypotecnibanka.cz/'
        self._price_realty = price_realty
        self._want_to_loan = want_to_loan
        self._time_debit = time_debit
        self._fixed_interest = fixed_interest
        self.repayment = self._calc_repayment()
        self.bank_margin = self._calc_bank_margin()

    def _calc_repayment(self) -> int:
        res = requests.post(
            url=self._url,
            data={
                "_mf_form_sent_": "classic_calc",
                "classic_realty_price": self._price_realty,
                "classic_loan_range": self._want_to_loan,
                "classic_period_of_repayment": self._time_debit,
                "classic_mortgage_insurance_switch": 1,
                "classic_mortgage_insurance_variant": 1,
                "classic_mortgage_insurance_percent": 100,
                "classic_fixation": self._fixed_interest,
            }
        )
        return self._get_repayment_from_response(html=res.text)

    def _get_repayment_from_response(self, html: str) -> int:
        soup = BeautifulSoup(html, 'html.parser')
        return int(soup.find(id='classic_repayment').get_text().replace(
            '\n', '').replace('\xa0', '').replace(' Kč', '').replace('↑↓', ''))

    def _calc_bank_margin(self):
        return self.repayment * self._time_debit * 12 - self._want_to_loan

    def __str__(self):
        return f"{self._price_realty},{self._want_to_loan},{self._time_debit},{self._fixed_interest},{self.repayment},{self.bank_margin}"
