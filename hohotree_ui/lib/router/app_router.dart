import 'package:flutter/material.dart';
import '../Screens/LoginScreen/loginScreen.dart';
import '../Screens/OnboardingScreen/onBoardingScreen.dart';
import '../Screens/HomeScreen/homeScreens.dart';
import '../Screens/registerScreen/registerScreen.dart';

abstract final class AppRouter {
  static const String login = '/login';
  static const String register = '/register';
  static const String root = '/';
  static const String msg = '/msg';
  static const String home = '/home';

  static Route<dynamic>? onGenerateRoute(RouteSettings settings) {
    switch (settings.name) {
      case root:
        // return MaterialPageRoute(builder: (_) => const onBoardingScreen());
        return MaterialPageRoute(builder: (_) => const LoginScreen());
      case login:
        return MaterialPageRoute(builder: (_) => const LoginScreen());
      case register:
        return MaterialPageRoute(builder: (_) => const RegisterScreen());
      case home:
        return MaterialPageRoute(builder: (_) => const HomeScreen());
      default:
        return MaterialPageRoute(builder: (_) => const onBoardingScreen());
    }
  }
}
