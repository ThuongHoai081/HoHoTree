import 'dart:async';

import 'package:flutter/material.dart';
import 'package:hohotree/Screens/HomeScreen/homeScreens.dart';
import 'package:hohotree/Screens/OnboardingScreen/widget/buildWidget.dart';
import 'package:smooth_page_indicator/smooth_page_indicator.dart';

class onBoardingScreen extends StatefulWidget {
  const onBoardingScreen({super.key});

  @override
  State<onBoardingScreen> createState() => _onBoardingScreenState();
}

class _onBoardingScreenState extends State<onBoardingScreen> {
  final PageController _controller = PageController();
  late Timer _timer; 

  @override
  void initState() {
    super.initState();
    _startAutoSlide();
  }

  void _startAutoSlide() {
    _timer = Timer.periodic(Duration(seconds: 2), (timer) {
      if (_controller.page == 3) {
        _controller.jumpToPage(0); 
      } else {
        _controller.nextPage(
          duration: Duration(milliseconds: 500),
          curve: Curves.ease,
        );
      }
    });
  }

  @override
  void dispose() {
    _timer.cancel();
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          PageView(
            controller: _controller,
            children: [
              buildPage(
                title: "Chào mừng đến với",
                subtitle: "HoHoTree",
                description1: "⭐ Ứng dụng tốt nhất năm 2025",
                description2: "🌱 cho chẩn đoán bệnh cây",
                description3: "👍 90%\nđánh giá tích cực",
                description4: "💊 1 triệu\ncây đã được chữa khỏi",
                backgroundWidget: Image.asset("images/backgroud.jpg", fit: BoxFit.cover),
              ),
              buildPage(
                title: "Tính năng chính",
                subtitle: "Xác định bệnh nhanh chóng",
                description1: "📸 Chụp ảnh để phân tích",
                description2: "💊 Gợi ý phương pháp điều trị",
                description3: "📊 Theo dõi tình trạng cây trồng",
                description4: "👥 Cộng đồng hỗ trợ & chia sẻ",
                backgroundWidget: Image.asset("images/bg3.jpg", fit: BoxFit.cover),
              ),
              buildPage(
                title: "Lợi ích của ứng dụng",
                subtitle: "Trợ thủ đắc lực cho nhà nông",
                description1: "⏳ Tiết kiệm thời gian & công sức",
                description2: "🔍 Xác định bệnh chính xác",
                description3: "📚 Kiến thức phong phú & cập nhật liên tục",
                description4: "🌿 Giúp cây trồng khỏe mạnh hơn",
                backgroundWidget: Image.asset("images/bg4.jpg", fit: BoxFit.cover),
              ),
              buildPage(
                title: "Hướng dẫn sử dụng",
                subtitle: "Chỉ 3 bước đơn giản",
                description1: "📷 Bước 1: Chụp ảnh cây trồng",
                description2: "🧐 Bước 2: Đợi AI phân tích bệnh",
                description3: "💡 Bước 3: Nhận kết quả & giải pháp",
                description4: "🚀 Thật dễ dàng phải không nào?",
                backgroundWidget: Image.asset("images/bg5.jpg", fit: BoxFit.cover),
              ),
            ],
          ),
          Positioned(
            bottom: 80,
            left: 0,
            right: 0,
            child: Center(
              child: SmoothPageIndicator(
                controller: _controller,
                count: 4, 
                effect: ExpandingDotsEffect(
                  activeDotColor: Colors.green,
                  dotColor: Colors.grey.shade300,
                  dotHeight: 8,
                  dotWidth: 8,
                ),
              ),
            ),
          ),
          Positioned(
            bottom: 30,
            left: 0,
            right: 0,
            child: Center(
              child: ElevatedButton(
                onPressed: () {
                  _timer.cancel(); 
                  Navigator.pushReplacement(
                    context,
                    MaterialPageRoute(builder: (context) => HomeScreen()),
                  );
                },
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.green,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(20),
                  ),
                  padding: EdgeInsets.symmetric(horizontal: 50, vertical: 15),
                ),
                child: Text("Bắt đầu", style: TextStyle(fontSize: 16)),
              ),
            ),
          ),
        ],
      ),
    );
  }
}