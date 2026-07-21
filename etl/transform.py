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

    dim_product.insert(
        0,
        "id",
        range(1, len(dim_product)+1)
    )

    dim_product_merge = dim_product.rename(
        columns={"id": "product_id"}
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

    dim_location.insert(
        0,
        "id",
        range(1, len(dim_location)+1)
    )

    dim_location_merge = dim_location.rename(
        columns={"id": "location_id"}
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

    dim_shipping.insert(
        0,
        "id",
        range(1, len(dim_shipping)+1)
    )
    
    dim_shipping_merge = dim_shipping.rename(
        columns={"id": "shipping_id"}
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

    dim_customer.insert(
        0,
        "id",
        range(1, len(dim_customer)+1)
    )

    dim_customer_merge = dim_customer.rename(
        columns={"id": "customer_id"}
    )

    fact_sales = df.merge(
        dim_product_merge,
        on=[
            "category",
            "sub_category"
        ],
        how="left"
    )

    fact_sales = fact_sales.merge(
        dim_location_merge,
        on=[
            "country",
            "city",
            "state",
            "postal_code",
            "region"
        ],
        how="left",
        suffixes=("", "_location")
    )

    fact_sales = fact_sales.merge(
        dim_shipping_merge,
        on=[
            "ship_mode"
        ],
        how="left",
        suffixes=("", "_shipping")
    )

    fact_sales = fact_sales.merge(
        dim_customer_merge,
        on=[
            "segment"
        ],
        how="left",
        suffixes=("", "_customer")
    )

    fact_sales = fact_sales[
        [
            "product_id",
            "location_id",
            "shipping_id",
            "customer_id",
            "sales",
            "quantity",
            "discount",
            "profit"
        ]
    ]

    return {
        "dim_product": dim_product,
        "dim_location": dim_location,
        "dim_shipping": dim_shipping,
        "dim_customer": dim_customer,
        "fact_sales": fact_sales
    }