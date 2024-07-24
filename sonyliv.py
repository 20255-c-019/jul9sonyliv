
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
      'Security_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MjE3OTc5MzEsImV4cCI6MTcyMzA5MzkzMSwiYXVkIjoiKi5zb255bGl2LmNvbSIsImlzcyI6IlNvbnlMSVYiLCJzdWIiOiJzb21lQHNldGluZGlhLmNvbSJ9.JtoXbcF_cjHWgydQ-2xQkkpChZBgRsFRidv0VoUEu6_qxV2fc6dpwwd3y_qRT2WWfi9UkZD5VfCmEHusJZ6vTVLCnh0a5wKXwctP0TYKxEuNcfSCFL5JbS6MgL18gZ0LbDA7DBxguAumr-Ck3E9f6YdVFnkpwMbaEkljw61ErvHONiCkE4gFEScbByWBpLu8RBQBecKI7uNIaSonWbQnGslj85bSrH359avMXKmryQZeHU56Zi8ygZXGz6BcBHcxw74blb3VY4x2Q5U490p61CYj0U01tJBsn4je4NmeXAZAwMYZA0YkW0EfhXsEmbZCbRwv-1OG0vpbWVZrlu58Kr_pXwnGqT8ZceTWtiBY9P3N1MpdGW0oOLoAcLm_Aao3NUL9UOlBF1JdGWbOuSimdsgKyhnvxSl_xRQfnnkbDC9vISjR21JXzXvyJNFetiOYsls16CIHrNGCUUaoVXtYChsEuBkO_Bvq2pd101cKlh7Ay1W0dOvPHPXffWoRelTj1jFNzadxLzpIAo1hg6rbKGIbNXwufsDOhoiCZJRDLJxtEYq6HIizXilqNmhksseB86bhHUVjX6y5T3FBLPO8x-EJcyzbwafF7Q4oSoAlZb_4UC5kyeK-sJSKeJ3fTie6fa-weEJREwuJ2u-aOeQyQismScELNlR1tuVfI5OMAOo',
      'Cookie': '_gcl_au=1.1.2051399265.1718769230; _fbp=fb.1.1718769230476.641955106222544936; _scid=c30f6459-24e8-4dce-abfd-b18014753039; afUserId=93915dc8-119a-4fff-b81c-48e6379a45d8-p; _cc_id=10005009d3a8df6f0c904c0087ff688f; WZRK_G=c112d060c2334041ab1d17732ddd974a; AF_SYNC=1721667305559; AKA_A2=A; bm_sz=604FF44DA272E9CB4470DB88DBF347F6~YAAQXXxBF2mHiL2QAQAA5dYo4xio3ZblcxKvPKu9j210IQV/qM4L+P6AgXSu9xQ8i175+saouVOgIlklY5qOd9GXX4za0o7zi37E4wfTuHNt0eYnDUxwf0oA/uflzyMuiWBMuP/D271G3RDAYGwwZ1BRxqGvq5gecZBEbKi5q9wv0suzcpOfSkJhhjofjRiQtB0pyofZA8v/k6qLmSkIFBr+xIuZZUKpeyzKRidrZN7lnG7Dz55e9yq5HLm8N0Kgjbkz/o8t4V7geb2z7onnR3hjV3FQHLwS6fk8+gDeeuCnhOmb9UWsi8kxmK0PGjuunZlmf+lwy/1+cgfjrSM+m3p/Q3bQMjGCPCBrTqTfktuEdXwPWboULKNcNubER3OC+XLoFPn8hmJlZwv+i6GOiXvnL1zeeQ==~3225668~3618372; sessionId=86ac6f9805a6454c9b2d9d1c55e447e9-Mozilla%2F5.0%2C(Macintosh%3B%2CIntel%2CMac%2COS%2CX%2C10_15_7)%2CAppleWebKit%2F537.36%2C(KHTML%2C%2Clike%2CGecko)%2CChrome%2F126.0.0.0%2CSafari%2F537.36; ak_bmsc=68DA84DBE97C9FE3EB422A4E9DFD8CD1~000000000000000000000000000000~YAAQXXxBF7iHiL2QAQAAzdgo4xhNyXkLklwyNdMj7qXqD/TsJEIuMbrnq68cFR/n19Ibe8EQJuBmwYnpo1xEggiLtRdjI78iZdigsSEuqA/RlKMT6Ujj4MwmcqFzzE+VLWnsxBe8/Jslivdq0V4qA/4lF/ovz9wkK8qpJlKtOO5sfKAgZgjpU0xm5JOZV8USP53ee4c8EakCKcuSSHx1JNyrmt++zc8xEvP3lOmgu4PjtWd83TEtFZN2taoZfY7Rv+DSL8gvbVe90b7jV8w/YifZ7Igbu2H4kK0zcg3VaSpjiyPcWBIsrbOHhuTOpGdXGNfIOqLbxcKCdMpK13NZD4OsHh9/O8DFzouPI47gXvGlaUUpVTFySQVTkr/kcroTEiA9UqCscgLiqBDMC5U4ALzN9y/TORLDDiTD1DqAxEW035o8tCzwr/tzhANbljujh8hnU/h498lD5qE=; __gads=ID=6464ebbd7c2540ed:T=1720467910:RT=1721798023:S=ALNI_MYpacyGQcolNGURgxUnSQLM7O8_qw; __gpi=UID=00000e871b6a7a21:T=1720467910:RT=1721798023:S=ALNI_MYoXeHiKC0EuckBmCbcJz4QLaSUgg; __eoi=ID=fb406118db27b6b2:T=1720467910:RT=1721798023:S=AA-AfjZGiVCjHbXdkVqDXuxnWyQZ; _scid_r=c30f6459-24e8-4dce-abfd-b18014753039; _ScCbts=%5B%5D; _ga=GA1.2.1813113485.1718769231; _gid=GA1.2.1227910760.1721798025; _dc_gtm_UA-34728540-15=1; WZRK_S_48K-8WW-754Z=%7B%22p%22%3A1%2C%22s%22%3A1721798022%2C%22t%22%3A1721798025%7D; panoramaId_expiry=1721884425332; panoramaId=dc37df2c79c01b76464ed5b8b4ffa9fb927a259f0fd802efdc845100a1084b78; panoramaIdType=panoDevice; _sctr=1%7C1721759400000; bm_sv=2A41EFCDB5C53795D6E55F29984394CB~YAAQXXxBF8KNiL2QAQAAuAQp4xj6k4ImPC008UIRI+V67HuUJR6QcVwA5+raN6oaIiMTnlhyDXv7J968M+5AkWd3D7TFvZssqz+8KREKnAwMsjEyRxJIeKdsORhqfZCYVekBbh8Yc91pOCZcqk6Ljs2IVEXVNfBx5B2vSz2DtkII++zrLRdWo+aheQqETRqCJ3hxtscxkEsr6s5gGIDJeZAaWiffz5qxGDGdmTTg7fT/ioNHCBLib/QqMuMZZcivd2I=~1; _abck=95D5F09874ACFA7EA58FE6FFC917A8C8~0~YAAQXXxBF2mTiL2QAQAArzEp4wxtYLJOTbT4uL8+cg60mw5qb712sm4IwenYRaLzudYbLdNavJeo9oWPqTRgLei8xN1wSoUNStiDzgeKN/I4hA31axE4xw+d2371kuRlnli9+o/2BPeS9qz1ZzL9qy4FzPMPzYHTNZ9sm7omlfHJsHnV/+XptHrRcdlS7r1XjeoNPjrbdAuC5uEwFkV6TF/muSQQKe5RY6JiBJYJGnlMiRoBAkBIcZaYiDsq5XUyGkwtex/52ZjG9l7py299f4k0pk3hwAucmUHGuMomFhXjyonpaYbDL4BH9Gv9RhUsRvcxuLNN1M6RH5tgY/Y4lEnlZy8yU/vUl90PbhH2Kx1aVqyh6pJLYIVaIk/thVDl0k4mRd6Un5tSnoCqgzMld9Ju9TwRbjikDkDBqjS3m5zwGcQaY9Ja+/OtTEEn4vk1xZleAkY=~-1~-1~-1; _ga_1WZE8VR8Q1=GS1.1.1721798023.12.1.1721798047.36.0.0'
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
