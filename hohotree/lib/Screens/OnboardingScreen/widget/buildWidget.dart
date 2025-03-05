import 'package:flutter/material.dart';

Widget buildPage({
  required String title,
  required String subtitle,
  required String description1,
  required String description2,
  required String description3,
  required String description4,
  Color backgroundColor = Colors.white,
  Widget? backgroundWidget,
}) {
  return Stack(
    children: [
      if (backgroundWidget != null) Positioned.fill(child: backgroundWidget),
      Center(
        child: Container(
          color: backgroundWidget == null ? backgroundColor : null,
          padding: EdgeInsets.all(20),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Image.asset('images/logo.png', height: 50),
              SizedBox(height: 10),
              Text(
                title,
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
              Text(
                subtitle,
                style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Colors.green),
              ),
              SizedBox(height: 30),
              Text(
                description1,
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ),
              Text(
                description2,
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 16),
              ),
              SizedBox(height: 20),
              Text(
                description3,
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ),
              SizedBox(height: 20),
              Text(
                description4,
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ),
            ],
          ),
        ),
      ),
    ],
  );
}
