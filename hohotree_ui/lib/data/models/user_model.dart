import 'package:json_annotation/json_annotation.dart';
part 'user_model.g.dart';

@JsonSerializable(createToJson: false)
class UserModel {
  UserModel({
    required this.id,
    required this.email,
    required this.fullName,
  });

  factory UserModel.fromJson(Map<String, dynamic> json) => UserModel(
        id: json['id'] as int,
        email: json['email'] as String?,
        fullName: json['full_name'] as String,
      );

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'email': email,
      'full_name': fullName,
    };
  }

  final int id;
  final String? email;
  final String fullName;
}