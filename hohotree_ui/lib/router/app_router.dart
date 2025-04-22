import 'package:flutter/material.dart';
import 'package:hohotree/Screens/MyPlantsScreen/MyPlantsScreen.dart';
import 'package:hohotree/Screens/PlantIssuesScreen/PlantIssuesScreen.dart';
import '../Screens/LoginScreen/loginScreen.dart';
import '../Screens/OnboardingScreen/onBoardingScreen.dart';
import '../Screens/HomeScreen/homeScreens.dart';
import '../Screens/registerScreen/registerScreen.dart';

abstract final class AppRouter {
  static const String login       = '/login';
  static const String register    = '/register';
  static const String root        = '/';
  static const String msg         = '/msg';
  static const String home        = '/home';
  static const String PlIs        = '/PlIs';
  static const String myT         = '/myT';
  static Route<dynamic>? onGenerateRoute(RouteSettings settings) {
    switch (settings.name) {
      case root:
        // return MaterialPageRoute(builder: (_) => const onBoardingScreen());
        return MaterialPageRoute(builder: (_) => const  onBoardingScreen());
      case login:
        return MaterialPageRoute(builder: (_) => const  LoginScreen());
      case register:
        return MaterialPageRoute(builder: (_) => const  RegisterScreen());
      case home:
        return MaterialPageRoute(builder: (_) => const  HomeScreen());
      case PlIs:
        return MaterialPageRoute(builder: (_) =>        PlantIssuesScreen());
      case myT:
        return MaterialPageRoute(builder: (_) =>        MyPlantsScreen());
      default:
        return MaterialPageRoute(builder: (_) => const  onBoardingScreen());
    }
  }
}
