// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'refresh_token_dto.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

RefreshTokenDTO _$RefreshTokenDTOFromJson(Map<String, dynamic> json) =>
    RefreshTokenDTO(
      accessToken: json['accessToken'] as String,
      refreshToken: json['refreshToken'] as String,
      expiresIn: (json['expiresIn'] as num).toInt(),
    );

Map<String, dynamic> _$RefreshTokenDTOToJson(RefreshTokenDTO instance) =>
    <String, dynamic>{
      'accessToken': instance.accessToken,
      'refreshToken': instance.refreshToken,
      'expiresIn': instance.expiresIn,
    };
