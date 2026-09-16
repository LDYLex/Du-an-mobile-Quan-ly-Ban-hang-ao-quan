import 'package:flutter/material.dart';
import 'package:quan_ly_ban_hang_ao_quan/tango.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: const Tango(),
      debugShowCheckedModeBanner: false,
    );
  }
}
