import pandas as pd
import plotly.express as px


class Data3D:
    def __init__(self, x: list, y: list, z: list, x_name=None, y_name=None, z_name=None):
        self.x = x
        self.y = y
        self.z = z
        self.x_name = x_name
        self.y_name = y_name
        self.z_name = z_name

    @staticmethod
    def create_from_dataframe(dataframe, col_name_x, col_name_y, col_name_z):
        return Data3D(
            x=list(dataframe[col_name_x]),
            y=list(dataframe[col_name_y]),
            z=list(dataframe[col_name_z]),
            x_name=col_name_x,
            y_name=col_name_y,
            z_name=col_name_z,
        )


def plot_3d_graph(data: Data3D):
    fig = px.scatter_3d(x=data.x, y=data.y, z=data.z, height=1300)
    fig.show()

def load_data_from_file(filename, z_name='repayment') -> Data3D:
    df = pd.read_csv(filename, sep=',')
    return Data3D.create_from_dataframe(df, 'want_to_loan', 'time_debit', z_name)


if __name__ == "__main__":
    # filename = 'res-2019-11-19_21_51_23.csv'
    filename = 'res-2019-11-19_23_12_13.csv'
    data_repayment = load_data_from_file(filename, z_name='repayment')
    data_bank_margin = load_data_from_file(filename, z_name='bank_margin')

    plot_3d_graph(data_repayment)
    plot_3d_graph(data_bank_margin)
