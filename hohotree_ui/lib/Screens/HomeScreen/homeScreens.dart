import 'dart:convert';
import 'dart:typed_data';
import 'dart:io';

import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:hohotree/Screens/HomeScreen/widget/buildBtn.dart';
import 'package:http/http.dart' as http;
import 'package:image_picker/image_picker.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  File? _imageFile;
  Uint8List? _imageBytes;
  String _result = "";

  Future<void> _pickImage() async {
    final picker = ImagePicker();
    final pickedFile = await picker.pickImage(source: ImageSource.camera);

    if (pickedFile != null) {
      if (kIsWeb) {
        final bytes = await pickedFile.readAsBytes();
        setState(() {
          _imageBytes = bytes;
        });
        await _analyzeImageWeb(bytes);
      } else {
        setState(() {
          _imageFile = File(pickedFile.path);
        });
        await _analyzeImage(_imageFile!);
      }
    }
  }

  Future<void> _analyzeImage(File imageFile) async {
    var request = http.MultipartRequest(
      'POST',
      Uri.parse('http://localhost:8000/api/plant/'),
    );

    request.files.add(await http.MultipartFile.fromPath('file', imageFile.path));
    var response = await request.send();
    var responseData = await response.stream.bytesToString();
    var jsonData = json.decode(responseData);

    setState(() {
      _result = jsonData['disease'] ?? 'Không xác định';
    });
  }

  Future<void> _analyzeImageWeb(Uint8List imageBytes) async {
    var request = http.MultipartRequest(
      'POST',
      Uri.parse('http://localhost:8000/api/plant/'),
    );

    request.files.add(http.MultipartFile.fromBytes('file', imageBytes, filename: 'image.jpg'));
    var response = await request.send();
    var responseData = await response.stream.bytesToString();
    var jsonData = json.decode(responseData);

    setState(() {
      _result = jsonData['disease'] ?? 'Không xác định';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          Positioned.fill(
            child: Image.asset(
              'images/bg9.png',
              fit: BoxFit.cover,
            ),
          ),
          Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 30),
                child: Text(
                  'Xác định một căn bệnh trong 1 cú nhấp chuột',
                  textAlign: TextAlign.center,
                  style: const TextStyle(
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                    color: Colors.white,
                  ),
                ),
              ),
              const SizedBox(height: 20),
              buildButton('Quét cây trồng', _pickImage),
              const SizedBox(height: 10),
              buildButton('Những vấn đề chung', () {}),
              const SizedBox(height: 20),
              if (_imageBytes != null && kIsWeb)
                Image.memory(_imageBytes!, height: 200)
              else if (_imageFile != null)
                Image.file(_imageFile!, height: 200),
              const SizedBox(height: 10),
              Text(
                _result.isNotEmpty ? _result : 'Kết quả sẽ hiển thị ở đây',
                style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white),
              ),
            ],
          ),
        ],
      ),
      bottomNavigationBar: BottomNavigationBar(
        backgroundColor: Colors.white,
        selectedItemColor: Colors.green,
        unselectedItemColor: Colors.grey,
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.search),
            label: 'Tìm cây',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.local_florist),
            label: 'Cây của tôi',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.settings),
            label: 'Cài đặt',
          ),
        ],
      ),
    );
  }
}
