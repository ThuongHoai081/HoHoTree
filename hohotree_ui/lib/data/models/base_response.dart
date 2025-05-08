import 'package:json_annotation/json_annotation.dart';
part 'base_response.g.dart';

@JsonSerializable(createToJson: false)

class BaseResponse {
  final int? statusCode;
  final String? message;
  final dynamic data;

  BaseResponse({
    this.statusCode,
    this.message,
    this.data,
  });

  factory BaseResponse.fromJson(Map<String, dynamic> json, {int? statusCode}) {
    return BaseResponse(
      statusCode: statusCode,
      message: json['message'],
      data: json['data'],
    );
  }
}
