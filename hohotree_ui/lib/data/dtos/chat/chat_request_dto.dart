import 'package:json_annotation/json_annotation.dart';
import '../../models/chat_model.dart';

part 'chat_request_dto.g.dart';

@JsonSerializable(createFactory: false)
class ChatRequestDTO {
  final List<ChatMessage> messages; // Danh sách tin nhắn

  ChatRequestDTO({
    required this.messages,
  });

  Map<String, dynamic> toJson() => _$ChatRequestDTOToJson(this);
}
