import 'package:flutter/material.dart';
import '../Screens/LoginScreen/loginScreen.dart';

abstract final class AppRouter {
  static const String login = '/login';
  static const String root = '/root';
  static const String addEditProduct = '/add_edit_product';

  static Route<dynamic>? onGenerateRoute(RouteSettings settings) {
    switch (settings.name) {
      case login:
        return MaterialPageRoute(builder: (_) => const LoginScreen());
      // case root:
      //   return MaterialPageRoute(builder: (_) => const ProductListScreen());
      // case addEditProduct:
      //   final product = settings.arguments as Product?;
      //   return MaterialPageRoute(
      //       builder: (_) => AddEditProductScreen(product: product));
      // default:
      //   return MaterialPageRoute(builder: (_) => const LoginScreen());
    }
  }
}
