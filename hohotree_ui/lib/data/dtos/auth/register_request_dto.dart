import 'package:json_annotation/json_annotation.dart';
part 'register_request_dto.g.dart';

@JsonSerializable(createToJson: true)
class RegisterRequestDTO {
  @JsonKey(name: 'full_name')
  final String fullName;
  final String email;
  final String password;

  RegisterRequestDTO({
    required this.fullName,
    required this.email,
    required this.password,
  });

  Map<String, dynamic> toJson() => _$RegisterRequestDTOToJson(this);
}
