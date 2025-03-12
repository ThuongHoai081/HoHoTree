import 'package:flutter/material.dart';
import 'package:hohotree/Screens/LoginScreen/loginScreen.dart';
import 'package:hohotree/Screens/OnboardingScreen/onBoardingScreen.dart';
import 'package:hohotree/Screens/registerScreen/registerScreen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
      ),
      home: RegisterScreen(),
    );
  }
}

