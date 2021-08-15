import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Simple app',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Simple app'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  double _size = 100;
  late double maxWidth;

  final int addConstant = 50;

  void _showSnackBarMessage(String message){
    ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(message),
        ),
      );
  }

  void _increaseSize() {
    if (_size + addConstant > maxWidth) {
      _showSnackBarMessage('Tamanho máximo atingido.');
    }else{
      setState(() {
        _size += addConstant;
      });
    }
  }

  void _decreaseSize() {
    if (_size < addConstant){
      _showSnackBarMessage('Tamanho mínimo atingido.');
    }else{
      setState(() {
        _size -= addConstant;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    maxWidth = MediaQuery.of(context).size.width;
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Expanded(
              child: Center(
                child: AnimatedContainer(
                  duration: Duration(milliseconds: 500),
                  width: _size,
                  height: _size,
                  color: Colors.blue,
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(20.0),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  IconButton(
                    onPressed: _decreaseSize,
                    icon: Icon(Icons.remove),
                  ),
                  IconButton(
                    onPressed: _increaseSize,
                    icon: Icon(Icons.add),
                  )
                ],
              ),
            )
          ],
        ),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
