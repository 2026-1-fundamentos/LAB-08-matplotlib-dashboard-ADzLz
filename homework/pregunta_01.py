# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    def load_data():
        """
        Carga el archivo CSV de datos de envíos.
        """
        df = pd.read_csv("files/input/shipping-data.csv")
        return df

    os.makedirs("docs", exist_ok=True)
    def create_visual_for_shipping_per_warehouse(df):
        """
        Crea un gráfico de barras para mostrar la cantidad de envíos por bloque de almacén.
        """
        df=df.copy()
        plt.figure()
        counts=df.Warehouse_block.value_counts()
        counts.plot.bar(
        title='Shipping per Warehouse',
        xlabel='Warehouse Block',
        ylabel='Record count',
        color='tab:purple',
        fontsize=9
        )
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.savefig("docs/shipping_per_warehouse.png")

    def create_visual_for_mode_of_shipment(df):
        """
        Crea un gráfico de barras para mostrar la cantidad de envíos por modo de envío.
        """
        df=df.copy()
        plt.figure()
        counts=df.Mode_of_Shipment.value_counts()
        counts.plot.pie(
        title='Mode of Shipment',
        wedgeprops={'edgecolor':'white',
                    'width':0.5},
        ylabel='',
        colors=['tab:orange','tab:blue','tab:green'],
        fontsize=9
        )
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.savefig("docs/mode_of_shipment.png")

    def create_visual_for_average_customer_rating(df):
        """
        Crea un gráfico de barras para mostrar la distribución de calificaciones de clientes.
        """
        df=df.copy()
        plt.figure()
        df=(
            df[['Mode_of_Shipment','Customer_rating']]
            .groupby('Mode_of_Shipment')
            .describe()
        )
        df.columns=df.columns.droplevel()
        df=df[['mean','min','max']]
        plt.barh(
            y=df.index.values,
            width=df['max'].values-1,
            left=df['min'].values,
            height=0.9,
            color='lightgray',
            alpha=0.8
        )
        colors=['tab:orange' if value>=3 else 'tab:blue'  for value in df['mean'].values]
        plt.barh(
            y=df.index.values,
            width=df['mean'].values-1,
            left=df['min'].values,
            height=0.5,
            color=colors,
            alpha=1.0
        )
        plt.title('Average Customer Rating')
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['left'].set_color('tab:gray')
        plt.gca().spines['bottom'].set_color('tab:gray')
        plt.savefig("docs/average_customer_rating.png")

    def create_visual_for_weight_distribution(df):
        """
        Crea un histograma para mostrar la distribución del peso de los envíos.
        """
        df=df.copy()
        plt.figure()
        df.Weight_in_gms.plot.hist(
        title='Shipped Weight Distribution',
        color='tab:purple',
        edgecolor='white',
        )
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.savefig("docs/weight_distribution.png")

    df = load_data()
    create_visual_for_shipping_per_warehouse(df)
    create_visual_for_mode_of_shipment(df)
    create_visual_for_average_customer_rating(df)
    create_visual_for_weight_distribution(df)

    html_content="""<!DOCTYPE html>
    <html lang="en">      
        <body>
            <h1 style="text-align:center">Shipping dashboard</h1>
            <div style="width:45%; float:left">
                <img src="../docs/shipping_per_warehouse.png" alt="Fig 1">
                <img src="../docs/mode_of_shipment.png" alt="Fig 2">
            </div>
            <div style="width:45%; float:left">
                <img src="../docs/average_customer_rating.png" alt="Fig 3">
                <img src="../docs/weight_distribution.png" alt="Fig 4">
            </div>
        </body>
    </html>"""
    with open("docs/index.html","w",encoding="utf-8") as f:
        f.write(html_content)