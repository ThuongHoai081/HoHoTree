import 'package:json_annotation/json_annotation.dart';

part 'chat_model.g.dart';

@JsonSerializable(createFactory: true, createToJson: true)
class ChatMessage {
  final String role; // "system", "user", "assistant"
  final String content;

  ChatMessage({
    required this.role,
    required this.content,
  });

  factory ChatMessage.fromJson(Map<String, dynamic> json) =>
      _$ChatMessageFromJson(json);
  Map<String, dynamic> toJson() => _$ChatMessageToJson(this);
}
