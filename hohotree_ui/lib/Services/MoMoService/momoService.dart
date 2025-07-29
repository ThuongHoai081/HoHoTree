import 'dart:convert';
import 'package:http/http.dart' as http;

class MomoService {
  static Future<String?> createMomoPayment(String amount) async {
    const url = "http://localhost:8000/api/create-momo/";

    final response = await http.post(
      Uri.parse(url),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"amount": amount}),
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      return data['payUrl'];
    } else {
      print("Error: ${response.body}");
      return null;
    }
  }
}
