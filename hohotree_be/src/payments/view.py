from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
import json
import uuid
import requests
import hmac
import hashlib

class CreateMoMoPayment(APIView):
    def post(self, request):
        endpoint = "https://test-payment.momo.vn/v2/gateway/api/create"
        accessKey = "F8BBA842ECF85"
        secretKey = "K951B6PE1waDMi640xX08PD3vg6EkVlz"
        orderInfo = "pay with MoMo"
        partnerCode = "MOMO"
        redirectUrl = "https://webhook.site/..."
        ipnUrl = "https://339d-2001-ee0-4b4b-4550-3cd1-3e5c-ccd7-fe00.ngrok-free.app/api/callback-momo/"
        amount = request.data.get("amount", "00000")
        orderId = str(uuid.uuid4())
        requestId = str(uuid.uuid4())
        extraData = ""
        partnerName = "MoMo Payment"
        requestType = "payWithMethod"
        storeId = "Test Store"
        autoCapture = True
        lang = "vi"
        orderGroupId = ""

        rawSignature = f"accessKey={accessKey}&amount={amount}&extraData={extraData}&ipnUrl={ipnUrl}&orderId={orderId}" \
                       f"&orderInfo={orderInfo}&partnerCode={partnerCode}&redirectUrl={redirectUrl}" \
                       f"&requestId={requestId}&requestType={requestType}"

        h = hmac.new(bytes(secretKey, 'ascii'), bytes(rawSignature, 'ascii'), hashlib.sha256)
        signature = h.hexdigest()

        data = {
            'partnerCode': partnerCode,
            'orderId': orderId,
            'partnerName': partnerName,
            'storeId': storeId,
            'ipnUrl': ipnUrl,
            'amount': amount,
            'lang': lang,
            'requestType': requestType,
            'redirectUrl': redirectUrl,
            'autoCapture': autoCapture,
            'orderInfo': orderInfo,
            'requestId': requestId,
            'extraData': extraData,
            'signature': signature,
            'orderGroupId': orderGroupId
        }

        response = requests.post(endpoint, json=data, headers={'Content-Type': 'application/json'})
        return Response(response.json(), status=status.HTTP_200_OK)
