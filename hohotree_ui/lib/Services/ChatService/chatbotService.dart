import 'package:dio/dio.dart';
import '../../data/dtos/chat/chat_request_dto.dart';
import '../../data/dtos/chat/chat_response_dto.dart';
import '../../data/models/chat_model.dart';
import '../../common/constants/endpoints.dart';

class ChatService {
  static Future<ChatResponseDTO> sendMessageToChatbot(String message) async {
    Dio dio = Dio();
    try {
      ChatMessage userMessage = ChatMessage(role: 'user', content: message);
      ChatRequestDTO requestDTO = ChatRequestDTO(messages: [userMessage]);

      final response = await dio.post(
        Endpoints.chat,
        data: requestDTO.toJson(),
      );

      if (response.statusCode == 200) {
        return ChatResponseDTO.fromJson(response.data); 
      } else {
        throw Exception('Error: ${response.statusCode}');
      }
    } catch (e) {
      print("Error: $e");
      throw Exception('Failed to send message');
    }
  }
}
