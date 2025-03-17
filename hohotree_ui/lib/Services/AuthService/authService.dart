import 'dart:convert';
import 'package:http/http.dart' as http;

class AuthService {
  static Future<String> register(String email, String password, String confirmPassword) async {
    if (password != confirmPassword) {
      return "Passwords do not match";
    }

    try {
      final response = await http.post(
        Uri.parse("http://localhost:8000/api/auth/register/"),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({
          "email": email,
          "password": password,
          "name": email.split('@')[0]
        }),
      );

      if (response.statusCode == 201) {
        return "Registration successful. Check your email to activate your account.";
      } else {
        return "Registration failed: ${jsonDecode(response.body)}";
      }
    } catch (e) {
      return "An error occurred: $e";
    }
  }

  static Future<String> login(String email, String password) async {
    try {
      final response = await http.post(
        Uri.parse("http://localhost:8000/api/auth/login/"),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({
          "email": email,
          "password": password,
        }),
      );

      if (response.statusCode == 200) {
        return "Login success";
      } else {
        return "Login failed: ${jsonDecode(response.body)}";
      }
    } catch (e) {
      return "An error occurred: $e";
    }
  }
}
