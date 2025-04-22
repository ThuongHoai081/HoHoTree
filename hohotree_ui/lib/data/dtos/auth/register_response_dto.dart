import '../../models/user_model.dart';
import 'package:json_annotation/json_annotation.dart';

part 'register_response_dto.g.dart';

@JsonSerializable(createToJson: false)
class RegisterResponseDTO {
  RegisterResponseDTO({required this.user});

  final UserModel user;

  factory RegisterResponseDTO.fromJson(Map<String, dynamic> json) =>
      _$RegisterResponseDTOFromJson(json);
}
