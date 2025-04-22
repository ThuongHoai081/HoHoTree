import 'package:flutter/material.dart';
import 'router/app_router.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
import 'common/constants/env_key.dart';

void main() async {
  await Supabase.initialize(
    url: EnvKeys.supabaseURL,
    anonKey: EnvKeys.supabaseAnonKey,
  );
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const MyApp());
}

final supabase = Supabase.instance.client;

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) => MaterialApp(
        debugShowCheckedModeBanner: false,
        initialRoute: AppRouter.root,
        onGenerateRoute: AppRouter.onGenerateRoute,
      );
}
