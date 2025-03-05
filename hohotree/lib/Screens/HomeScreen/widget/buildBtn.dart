import 'package:flutter/material.dart';

Widget buildButton(String text) {
  return SizedBox(
    width: double.infinity, // Đảm bảo button có cùng chiều rộng
    child: Padding(
      padding: const EdgeInsets.symmetric(horizontal: 50),
      child: ElevatedButton(
        style: ElevatedButton.styleFrom(
          backgroundColor: Colors.white, // Màu nền trắng
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(30),
          ),
          padding: EdgeInsets.symmetric(vertical: 15),
          elevation: 2, // Đổ bóng nhẹ
        ),
        onPressed: () {},
        child: Text(
          text,
          style: TextStyle(
            color: Color.fromARGB(255, 7, 140, 27), // Màu chữ xanh lá
            fontSize: 16,
            fontWeight: FontWeight.bold, // Đậm hơn để giống ảnh
          ),
        ),
      ),
    ),
  );
}

