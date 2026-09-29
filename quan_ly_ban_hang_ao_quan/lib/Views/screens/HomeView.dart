import 'package:flutter/material.dart';

class Homeview extends StatelessWidget {
  const Homeview({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Column(
          children: [
            Row(
              children: [
                const SizedBox(height: 50),

                IconButton(onPressed: () {}, icon: const Icon(Icons.menu)),
                const SizedBox(width: 40),

                Container(
                  width: 200,
                  height: 30,
                  child: TextField(
                    style: const TextStyle(fontSize: 12),
                    decoration: InputDecoration(
                      hintText: "Tìm kiếm sản phẩm",
                      hintStyle: const TextStyle(fontSize: 12),
                      prefixIcon: const Icon(Icons.search, size: 18),
                      contentPadding: const EdgeInsets.symmetric(vertical: 10),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(20),
                      ),
                    ),
                  ),
                ),
                IconButton(onPressed: () {}, icon: Icon(Icons.abc)),
              ],
            ),
            Row(
              children: [
                Expanded(
                  child: Column(children: [Image.asset(""), Text("Ao phong")]),
                ),
                Expanded(
                  child: Column(children: [Image.asset(""), Text("Ao phong")]),
                ),
                Expanded(
                  child: Column(children: [Image.asset(""), Text("Ao am")]),
                ),
                Expanded(
                  child: Column(
                    children: [Image.asset(""), Text("Ao tay dai")],
                  ),
                ),
                Expanded(
                  child: Column(children: [Image.asset(""), Text("quan tay")]),
                ),
                Expanded(
                  child: Column(children: [Image.asset(""), Text("quan bo")]),
                ),
              ],
            ),
            Row(
              children: [
                Expanded(
                  child: Row(
                    children: [
                      Text(
                        "Danh cho ban",
                        style: TextStyle(color: Colors.black, fontSize: 15),
                      ),
                      const SizedBox(width: 10),
                      Text(
                        "Gan ban",
                        style: TextStyle(color: Colors.black, fontSize: 15),
                      ),
                      const SizedBox(width: 10),
                      Text(
                        "Moi nhat",
                        style: TextStyle(color: Colors.black, fontSize: 15),
                      ),
                      const SizedBox(width: 10),
                      Text(
                        "video",
                        style: TextStyle(color: Colors.black, fontSize: 15),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
      bottomNavigationBar: Row(
        children: [
          IconButton(onPressed: () {}, icon: Icon(Icons.home)),
          IconButton(onPressed: () {}, icon: Icon(Icons.chat)),
          IconButton(onPressed: () {}, icon: Icon(Icons.person)),
        ],
      ),
    );
  }
}
