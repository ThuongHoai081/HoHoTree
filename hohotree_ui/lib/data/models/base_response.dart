import 'package:json_annotation/json_annotation.dart';
part 'base_response.g.dart';

@JsonSerializable(createToJson: false)
class BaseResponse {
  final String? message;
  final String? status;

  BaseResponse({this.message, this.status});

  factory BaseResponse.fromJson(Map<String, dynamic> json) {
    return BaseResponse(
      message: json['message'],
      status: json['status']?.toString(),
    );
  }
}
