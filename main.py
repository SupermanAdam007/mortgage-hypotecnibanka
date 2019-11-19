import datetime

from mortgage import MortgageRequest


def append_configuration_to_file(row, filename='res.csv'):
    with open(filename, 'a') as f:
        f.write(row)


def get_mortgage_row(price_realty, want_to_loan, time_debit) -> str:
    mortage_req = MortgageRequest(price_realty, want_to_loan, time_debit)
    return f"{str(mortage_req)}\n"


if __name__ == "__main__":
    filename = f"res-{datetime.datetime.now():%Y-%m-%d_%H_%M_%S}.csv"

    append_configuration_to_file(
        'price_realty,want_to_loan,time_debit,fixed_interest,repayment,bank_margin\n',
        filename=filename)

    for want_to_loan in range(1180000, 1730000, 50000):
        for time_debit in range(5,31):
            mortage_row = get_mortgage_row(
                price_realty=2180000,
                want_to_loan=want_to_loan,
                time_debit=time_debit
            )
            append_configuration_to_file(mortage_row, filename=filename)
