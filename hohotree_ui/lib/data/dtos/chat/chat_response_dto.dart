import 'package:json_annotation/json_annotation.dart';

part 'chat_response_dto.g.dart';

@JsonSerializable(createToJson: false)
class ChatResponseDTO {
  final String response;  // Nội dung trả lời từ chatbot

  ChatResponseDTO({required this.response});

  factory ChatResponseDTO.fromJson(Map<String, dynamic> json) =>
      _$ChatResponseDTOFromJson(json);
}
