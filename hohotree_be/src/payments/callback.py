from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
class CallBackPayment(APIView):
    def post(self, request):
        data = request.data

        result_code = data.get("resultCode")
        order_id = data.get("orderId")
        message = data.get("message")

        if result_code == 0:
            print(f"Thanh toán thành công cho orderId: {order_id}")
            return Response({"message": "Thanh toán thành công."}, status=status.HTTP_200_OK)
        else:
            print(f"Thanh toán thất bại: {message}")
            return Response({"message": "Thanh toán thất bại."}, status=status.HTTP_400_BAD_REQUEST)
