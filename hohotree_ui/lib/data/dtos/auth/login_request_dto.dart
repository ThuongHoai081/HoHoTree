import 'package:json_annotation/json_annotation.dart';
part 'login_request_dto.g.dart';

@JsonSerializable(createFactory: false)
class LoginRequestDTO {
  LoginRequestDTO({
    required this.email,
    required this.password,
  });
  final String email;
  final String password;

   Map<String, dynamic> toJson() => _$LoginRequestDTOToJson(this);
}