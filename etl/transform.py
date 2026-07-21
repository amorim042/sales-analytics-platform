import pandas as pd

def transform_sales_data(df: pd.DataFrame):
    df = df.rename(columns={
        "Ship Mode": "ship_mode",
        "Segment": "segment",
        "Country": "country",
        "City": "city",
        "State": "state",
        "Postal Code": "postal_code",
        "Region": "region",
        "Category": "category",
        "Sub-Category": "sub_category",
        "Sales": "sales",
        "Quantity": "quantity",
        "Discount": "discount",
        "Profit": "profit"
    })

    dim_product = (
        df[
            [
                "category",
                "sub_category"
            ]
        ]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    dim_location = (
        df[
            [
                "country",
                "city",
                "state",
                "postal_code",
                "region"
            ]
        ]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    dim_shipping = (
        df[
            [
                "ship_mode"
            ]
        ]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    dim_customer = (
        df[
            [
                "segment"
            ]
        ]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    return {
        "dim_product": dim_product,
        "dim_location": dim_location,
        "dim_shipping": dim_shipping,
        "dim_customer": dim_customer,
        "fact_sales": df
    }