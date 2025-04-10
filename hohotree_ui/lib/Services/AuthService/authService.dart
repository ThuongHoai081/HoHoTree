import 'dart:convert';
import 'package:hohotree/data/dtos/auth/login_request_dto.dart';
import '../../common/constants/endpoints.dart';
import 'package:http/http.dart' as http;
import '../../data/dtos/auth/register_request_dto.dart';
import '../../common/util/dio.dart';
import 'package:dio/dio.dart';
import '../../data/models/base_response.dart';

class AuthService {
  static Future<BaseResponse> register(RegisterRequestDTO data) async {
    try {
      final response = await DioClient.dio.post(
        Endpoints.register,
        data: data.toJson(),
      );

      return BaseResponse.fromJson(response.data);
    } on DioException catch (e) {
      return BaseResponse(
        statusCode: e.response?.statusCode ?? 500,
        message: e.response?.data["message"] ?? e.message,
      );
    } catch (e) {
      return BaseResponse(
        statusCode: 500,
        message: "An unexpected error occurred: $e",
      );
    }
  }

  static Future<BaseResponse> login(LoginRequestDTO data) async {
    try {
      final response = await DioClient.dio.post(
        Endpoints.login,
        data: data.toJson(),
      );

      return BaseResponse.fromJson(response.data);
    } on DioException catch (e) {
      return BaseResponse(
        statusCode: e.response?.statusCode ?? 500,
        message: e.response?.data["message"] ?? e.message,
      );
    } catch (e) {
      return BaseResponse(
        statusCode: 500,
        message: "An unexpected error occurred: $e",
      );
    }
  }
}
