
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
      'Security_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MjMzODE4NTQsImV4cCI6MTcyNDY3Nzg1NCwiYXVkIjoiKi5zb255bGl2LmNvbSIsImlzcyI6IlNvbnlMSVYiLCJzdWIiOiJzb21lQHNldGluZGlhLmNvbSJ9.SyPUhNyrFTMsyf-sh2lrO0X4ja5Br0k4nGtPWFivaVOdzVNDshavG6fQ4DY4f_56OWxOf5e2ApN05N_VQUiJKnnCMLLcV9G0zJ5TFFfFszOLkymjLxNmogWl8vsKNwbo5Z2m_j2bQ0blHWbD1GRi4_Xs9PlRHhqYM49Wa4xF5zIv0e-K7t5WTEZXPL0bm7DJO4cnyMOAFI_kxoPT6NfhephnuVyoM7Wogh8tUktH9j0fE7Ju0bimKslSJnw6om43iHhq45_g16ekbi1DZFy5HIx6O_Xg6waec_Ru4SDkKZzixVURf3-Ni0gtITabZqQfgpOM78o26HUHLSVkw5GsamyJREAOFiS6fVo3Thb-DYBpl2_kxnqRh5VuX02I1vXxmN7oAikvtnOIlzvlkxoItgObOQAxCyWSQs6q98bYNfkiUx9OvNWR6GW9UESWSDDeUeaZYtDDt1zlKThQFh7CgxQlJEqYJRbTErA9JJf_KK8-nTJWy8pBDf9SFFuAxHLXn3hABLeutB1cHDV_RuNQrZEARfXsHzX_BIqVTIYbFfffDUsayMPH2ZK0DEzr6UPHjElmOjTy2cI3MAAxYEqAPU221odHDnICMNmewRNuzzZRVcy5tN1qdOn34srntTHMEBYmxbTOISmm78DWyU98gE6UOQI-_Nngbojg_QxoZHE'
      'Cookie': '_gcl_au=1.1.2051399265.1718769230; _fbp=fb.1.1718769230476.641955106222544936; _scid=c30f6459-24e8-4dce-abfd-b18014753039; afUserId=93915dc8-119a-4fff-b81c-48e6379a45d8-p; _cc_id=10005009d3a8df6f0c904c0087ff688f; __gads=ID=6464ebbd7c2540ed:T=1720467910:RT=1721798023:S=ALNI_MYpacyGQcolNGURgxUnSQLM7O8_qw; __gpi=UID=00000e871b6a7a21:T=1720467910:RT=1721798023:S=ALNI_MYoXeHiKC0EuckBmCbcJz4QLaSUgg; __eoi=ID=fb406118db27b6b2:T=1720467910:RT=1721798023:S=AA-AfjZGiVCjHbXdkVqDXuxnWyQZ; AF_SYNC=1723220874291; _ScCbts=%5B%22442%3Bchrome.2%3A2%3A5%22%5D; panoramaId=f13d4f656d6ca198d92f6f9fe27c185ca02c405bee74001b9e396fb3f2446aea; panoramaIdType=panoDevice; _sctr=1%7C1723141800000; WZRK_G=4babda82c8504bd9b2af3e94585bd013; AKA_A2=A; bm_sz=27A07FEF73DF220197A636A476A068F1~YAAQlnUsMdFdeDORAQAAkmiSQRi0oFe418Km0dDaQ6JMKkG+ImucHvQd1UTbjckDowQThSsW54p5G+CgjrLUHjYmbUD26d/JbFX2BdTibTU2GJRUYyuqZbXiL29NkxVIjfQnLW2Nq4shmGpKtdN5btoJsxZj80D9oagoG/1ALFDiD006tPwV5y47Xz6ChT303x3Q0o6rmRFpleFOd3IXfngLJTqTFR/f5SgJD0wjly96lj291PiimdxC4kVL6M/iz/yePyqvCPEa5dxOfizRYfngZlbWut4yPDeC9DJNaatDZJLZ5hZtvFX7Tw+9ERNPelm6MllDILRgK4qmewzAADhbV+XmrviW51K3c4ZQTGAG8XHXQcD/Rlsx98b9+WfYbOPz4/HQffhOG+COTUHH7ekpX/A=~3490358~3553589; ak_bmsc=CB4C65DF7BA8C0A0A9E1F1ACE0D82219~000000000000000000000000000000~YAAQlnUsMeBdeDORAQAAO2mSQRiz9BKl8Af6CUoxvb3hM33ld4WaeZRZqG3lBwoXaoKpZEMd4DKxd452Eld76Q7f7SxE01XuUxLlaf42EVZbWW+03dtSdpCmIkBMndqv7fKuUpFekGJCqWRTdVKF9eQguuL7qZqBscU9PmgBok0AwOv8NLAZVSq/GS9jlrs8gr7IIVPL5cTgT4Dd9WsLnZntIsfMUD3eUdcpN7Xiw5l2smP4NDQY0aQmQ/cA8ztO/UGOr4UoTihGCvlhmVIGRNs+1O4VF+IbyD855dAbnsJVlhYjTswN3+WPlZT2qdIGSWG79zqkTVBx90GnzzUvRD0YChnCxVJjrK7LOyEgsh+m4vKsvqUOoEeD3vwa5MoUkgoIhl9K4eaALRSStEd1KJxTfYtu2OnKIoIInBq4BmSO+/lHE2mID3tM5W32SQPYspZzCdgiT2CYdmv0WITnYws9lTxbNyE8hssjk+aw8ow=; sessionId=5f70a3ca5b0b428895bf92f6d1ab61a5-Mozilla%2F5.0%2C(Macintosh%3B%2CIntel%2CMac%2COS%2CX%2C10_15_7)%2CAppleWebKit%2F537.36%2C(KHTML%2C%2Clike%2CGecko)%2CChrome%2F127.0.0.0%2CSafari%2F537.36; _scid_r=c30f6459-24e8-4dce-abfd-b18014753039; panoramaId_expiry=1723986801633; _ga=GA1.2.1813113485.1718769231; _gid=GA1.2.1334933304.1723382002; _dc_gtm_UA-34728540-15=1; WZRK_S_48K-8WW-754Z=%7B%22p%22%3A1%2C%22s%22%3A1723381998%2C%22t%22%3A1723382009%7D; _abck=95D5F09874ACFA7EA58FE6FFC917A8C8~0~YAAQlnUsMWNheDORAQAAK7ySQQw+1zrw9YMDSVBS4pNoq9qrXl3phAXl2xSEx1ThoB44GjIAMEtybI6r8L0grZxxmJBNosqRMsGomQWlwMUtJ8WShHErAK8En7rSYPm8e6WhaoQZwGEfUIold478YdOSoUW88veVifknu1hs+QAeLnHeWhfOPUH9fqxz0xIu8gmhSDVgeRWG0TzzqQ+JUfXVcqhvRrWR2g/NmaIm2GGBLuy5fbMjjhC7uw6fiXXVKFiMoCM1aS+b7Vam+Y2F40dub38C5yXMQY6EJY+jVKvb2Q4gAkJX1WTRaAUn0n5UoG2Ip6iUKaS93sYhiGJETU2n8/7420LEUrOzonMxYaHpStyo2wovlQlnrysxbUE4lrKawiMyhEmHZ8hjHns74Xknf86Q/FKvSe+f2O2FClrApKkqTqU9yW90ARYng0KjtF3N9TKVlGhUHk9Xk0KYdljjpye6+to4GT4eCQzAn292PwwIBtBIjH+PCch7nzWnFQ==~-1~-1~-1; _ga_1WZE8VR8Q1=GS1.1.1723382000.18.1.1723382021.39.0.0; bm_sv=0ADE7B160B1E297C27E3D9D1E7480943~YAAQlnUsMcRheDORAQAAuMKSQRjInmymJLrLZnThIdjc5HUbJWEQ5VktV5XxeCft1JPlvdED0viMRkk8KjNSx3bvVUFXB91L7EJQdhxPDBylEnyB/QFmcv3uFcUhNiJad1LpWAwzXqWkbCkVqbQoBeQdSepSalXf21rX7JIHCH8zZ/KJy4/SXja7ufQBHoTbG0IFPIzSAhH1m/wT7IXLHhEq+TRunEvj+bFwdA3DY4/PX1r4FtpzELX9ltJJRuzuLg==~'
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
