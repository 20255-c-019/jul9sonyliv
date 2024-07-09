
import time
import requests
import json
css = """
<style>
.gradient-text {
display: flex;
    justify-content: center;
    align-items: center;
    height: 36px; /* Adjust height as needed */
    background: linear-gradient(to right, #00c6ff, #0072ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 36px;
    font-weight: bold;
    padding: 20px;
    padding-top:0px;
    margin:0px;
    padding-bottom: 0px;
    border-radius: 10px;

}
.gradient-button {
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    font-weight: bold;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.gradient-button:hover {
    opacity: 0.9;
    transform: translateY(-1px);
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
}
</style>
"""
def serverrequest(data):


    url = "https://apiv2.sonyliv.com/AGL/1.7/SR/ENG/WEB/IN/SUBSCRIPTION/PRODUCTSBYCOUPON"

    payload = {'voucherCode': data,
    'channelPartnerID': 'MSMIND'}
    files=[

    ]
    headers = {
      'Security_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MjA0OTYzNjMsImV4cCI6MTcyMTc5MjM2MywiYXVkIjoiKi5zb255bGl2LmNvbSIsImlzcyI6IlNvbnlMSVYiLCJzdWIiOiJzb21lQHNldGluZGlhLmNvbSJ9.GSDfjpWcqjH9n9UV1I0pmF7vgk9zfXDldGEyJztoaXUzxb4tHpWnky9sTYK4aCMxQl9WrqX0_49clDlrzho6n3LHctuuBW80aGHE471fNV1E08Etn-gSTycRaKGU1qrQZ6at4ipyB89z2UIGXElwtaEdGTDchV91nKKueEI43IBSDTsNPxQCYkIRiwTuAVUtiBBQbuuB1P6Bn50xY4dL4i9bqerGsnV9H9xgag1mcjG2R2eldwYRzeZusBVVYFV2RoutD_CRvnsx2VdPVBapq88ekybO8Kiq_CxL-EmpKGtPP-l1k_CXBnz4wTbBUL_xLW1jZoNxbOfg0GNimgZITxUu2NMfrjwSYTqQjDJHNFBxNbInEhwaydwQNKzqA2pHY5pnfh9R45Vk7oSBHoOI1ASIDAsQEO4l5vDVZYwhZh6xBl2nSmm_W3YTk-SV_zSGh3GHv5jmkleyVd_6Rfpwa8aeJ2-0yzVARKLkoKxRrak6xRounUcOMXhiSG9fZc93PVHZB1e5CIJUJphsvfcQums4bdIkAAUrKeBGITrSFZSTLYel3gNa8p5k4hUjioUbPv2-8JixwzWNW90hvk-pLAnCRAKdZ-IydKZg0ZC61hrNy7m76FHxi1KSIDEJQxREAArwkwP4PUblM0dxZCosBmDZMOwopsuLERdqyHa2juM',
      'Cookie': '_gcl_au=1.1.2051399265.1718769230; _fbp=fb.1.1718769230476.641955106222544936; _scid=c30f6459-24e8-4dce-abfd-b18014753039; afUserId=93915dc8-119a-4fff-b81c-48e6379a45d8-p; _cc_id=10005009d3a8df6f0c904c0087ff688f; _ScCbts=%5B%5D; _sctr=1%7C1719945000000; AF_SYNC=1720008549925; panoramaIdType=panoDevice; panoramaId=dc37df2c79c01b76464ed5b8b4ffa9fb927a259f0fd802efdc845100a1084b78; _gid=GA1.2.2117696727.1720467904; AKA_A2=A; ak_bmsc=D78AF2164C0920A985AC5C806BA57C5F~000000000000000000000000000000~YAAQTXxBFyMpBmCQAQAAznSClRjIfGsYftIJIcPR+PkoXbI/TjWmI+9jtyH/RVmcWa2iuStg4Vi9G9qWptylXkt/ppKoTlvF8rJbr5GQBdZ84pNLm6OOgtQSfN6y0ILrM3qhS23EECvx47AZxayB831Udc8BB+P9eDPtH8RrCZo7G/gdykCUREBVMGwsA5769z49rs2D+CIDqhEhj+rgB/4Ph5TGOjL4geavDETNPgriHfcULMEqlRvlf8O4Zi8SlRJQtZS4oqkxjGecMa9nAFYpBqTMDsPwHvQnqmcMim18pBkie3zwGizOXjpykCQ+7f5lQLPlV75UfaIATbWPFY8hwXr/TOkLHFfGvoKzUwYTY89r/xNW3M9Iw9PgP8v8uZ/OjM2e/q/3EGsmIjk94K+LCoB0endcmiXBlzmyOYIh26aGSlwEyQsiq9YYOHBgQjhtlPe3l/8Jwg==; WZRK_G=c112d060c2334041ab1d17732ddd974a; bm_sz=693A04FFCA10D6105DC1B5C41DA0A603~YAAQTXxBF/hkCWCQAQAADdCTlRgAiAaUYSCXN9WHujP1X2JhyMm/C51x7p8hrwL/0ObpcDxQnokPgb5zCQicPnEZiBIIHj13jqromsJI/6geI3bxzGmU/13IAiTOhu6Wr2TJfMQ9EEG8xj9lgYKBUHuoc63ankp1iR3odjbuMqweyv8rRnDGPU35lm+IXe4Q0U5RZ3kNmFRcx+Fu6TakAWrS9YedKHhHH+hH9fJwBOLqtL4ViyUmgOwv+7jnD0OD0NCBPUGdp+CIDnXT+/ZgDWZNwO20Fatxg4Ujr9y5svhsb+sYU6jU+iqgCVY/CrIEn9uVjto5EEMB3nRZurueg83Qrl9xT0JfdeqhLJUfWlEKTSDZYctakjkbVPkKWPWxSX6+uqOOhkKaHMddyhNER/O8CLDL3NRFuWJdqvVm1Zs=~4470323~3616816; __gads=ID=6464ebbd7c2540ed:T=1720467910:RT=1720496411:S=ALNI_MYpacyGQcolNGURgxUnSQLM7O8_qw; __gpi=UID=00000e871b6a7a21:T=1720467910:RT=1720496411:S=ALNI_MYoXeHiKC0EuckBmCbcJz4QLaSUgg; __eoi=ID=fb406118db27b6b2:T=1720467910:RT=1720496411:S=AA-AfjZGiVCjHbXdkVqDXuxnWyQZ; _scid_r=c30f6459-24e8-4dce-abfd-b18014753039; sessionId=a0acb30e37984aea8a4f7f067981b89c-Mozilla%2F5.0%2C(Macintosh%3B%2CIntel%2CMac%2COS%2CX%2C10_15_7)%2CAppleWebKit%2F537.36%2C(KHTML%2C%2Clike%2CGecko)%2CChrome%2F126.0.0.0%2CSafari%2F537.36; panoramaId_expiry=1720582812132; _ga=GA1.2.1813113485.1718769231; _dc_gtm_UA-34728540-15=1; WZRK_S_48K-8WW-754Z=%7B%22s%22%3A1720495300%2C%22t%22%3A1720496412%2C%22p%22%3A1%7D; _abck=95D5F09874ACFA7EA58FE6FFC917A8C8~0~YAAQTXxBF9VmCWCQAQAAX9mTlQwlByxtNrcRj8yk4oYDGdnR9roMafr0ROIn0XgyOlg6HXydHsKPp6mKWWtx7l9JA96xSCZWNBvAKUguvYGt6g3vnLiWY6d1Oo0/nPnj6BoA2vIICaGHBXt1XhbxooQBYG/Ws0mc1EaaWvA7jcr2+Cec2lA24DtddsfIQgtIkG7uVHW3WaLJt6fKMWmBjAjQ9yBL/62ylnLJ+qy5a06lcGiyeozQcIF1ywplRl6NhD1szRq4c+VcxyKGmWx92LytRr4AY1ESa4fploORuvspj7iJd981frfHrIsbHrP/PvmOVVbSjYz7FxcELsaQdMRf6dBWXyMWwdvjfalYQKbj3ZVlSnaytDp0z7HtYLRbVpyIs9o9ndFfSWrCJuK+QI2WfbwUgDIjsz7mIcdRTdEYn2X3BBYWTO26pFV+2aZG4R9KzJk=~-1~-1~-1; _ga_1WZE8VR8Q1=GS1.1.1720495273.8.1.1720496424.47.0.0; bm_sv=EBFAF553B54F34AF3F48B2C394736F74~YAAQTXxBF4ZvCWCQAQAAQgeUlRhxZfJbZ+khnP0lFUcw2JSxQJpVSuMwTlFLajBtg7HGkUF/UuOnsJEbAvUaXigF3iwzZ0RsiX5IGWTzd4eQYO4QmJdNMlgQaNSsHryARMvx/CUsNfjF+UzNLxIU1fri1e+maHlxQqUP+FdgaI7+6QZnW2ZaYBZCtDvF6u7sdaerEirExxgjYNEV2sEkRd8v5YRw/5ILoH1zopAu/TA9Yi7057wrj2c3voJyqkt2ftM=~1'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)
    return response.text



def checkcode(codes_array):
    check_response=[]
    for code in codes_array:

        time.sleep(1)
        api=json.loads(serverrequest(code))
        response=""
        if(api["message"]==""):
            response= "successful coupon appiled "
        else:
            response=api["message"]
        print(api["message"])


        check_response.append(response)
    return check_response


import streamlit as st

st.markdown("""
<style>
          h1{  text-align: center;
            color: #fff;
            /* Change the color to white to match the gradient */
            margin: auto
            margin-top: 20px;
            margin-bottom: 20px;
            font-weight: bold;
            text-transform: capitalize;
            /* Add animation styles */
            background-image: linear-gradient(-225deg, #231557 0%, #44107a 29%, #ff1361 67%, #fff800 100%);
            background-size: auto auto;
            background-clip: border-box;
            background-size: 200% auto;

            background-clip: text;
            -webkit-background-clip: text;
            text-fill-color: transparent;
            -webkit-text-fill-color: transparent;
            animation: textclip 2s linear infinite;
            text-transform: uppercase;
            font-size: 20px;
            margin :0px;
            padding-bottom :0px
            }
            </style>

            """, unsafe_allow_html=True)
# Display the styled heading
st.markdown(css, unsafe_allow_html=True)
st.markdown('<p class="gradient-text">OTT CONNECT</p>', unsafe_allow_html=True)

st.markdown("<h1> SONYLIV CHECKER </h1>", unsafe_allow_html=True)
st.markdown(css, unsafe_allow_html=True)

codes_txt = st.text_area("", height=180)

if st.button("submit"):
   codes_array = codes_txt.splitlines()
   print(codes_array)
   data =checkcode(codes_array)
   i=0
   for code in data:
       if code == "successful coupon appiled ":
           st.markdown(
               '<p style="background-color: green; color:white;padding: 10px; border-radius: 5px;">'+codes_array[i]+"                        "+code+'</p>',
               unsafe_allow_html=True)
       else:
           st.markdown(
               '<p style="background-color: red; padding: 10px;color:white; border-radius: 5px;">' + codes_array[
                   i] + "                        " + code + '</p>',
               unsafe_allow_html=True)

       i+=1
