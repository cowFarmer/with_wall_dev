import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:with_wall/component/search.dart';
import 'package:with_wall/const/colors.dart';
import 'package:with_wall/component/center_info.dart';
import 'dart:convert';


class CenterListScreen extends StatelessWidget {
  final List<int> numbers = List.generate(100, (index) => index);
  var _PlaceList;

  GetCenterList() async {
    final routeFromJsonFile = await rootBundle.loadString('asset/center_list_json/center_list_json.json')
    _PlaceList = PlaceList.fromJson(routeFromJsonFile).places ?? <Place>[];
    print(_PlaceList);
  }



  CenterListScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        body: Column(
          children: [
            Expanded(
              flex: 1,
              child: Search(),
            ),
            Expanded(
              flex: 15,
              child: SingleChildScrollView(
                physics: ClampingScrollPhysics(),
                child: Column(
                  children: numbers
                      .map(
                        (e) => CenterInfo(
                          centerNumber: e,
                        ),
                      ).toList(),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget renderCenter(e) {
    return Container(
      height: 100,
      decoration: BoxDecoration(
        border: Border.all(color: PRIMARY_COLOR),
      ),
      child: Center(
        child: Text(e.toString()),
      ),
    );
  }
}

// json -> object
class Place {
  String? store_name;
  String? naver_category;
  String? address;
  String? naver_map_url;
  String? main_img_url;
  String? price_list;
  String? open_time_list;
  String? level_list;
  String? change_time_list;

  Place ({
    this.store_name,
    this.naver_category,
    this.address,
    this.naver_map_url,
    this.main_img_url,
    this.price_list,
    this.open_time_list,
    this.level_list,
    this.change_time_list,
  });

  factory Place.fromJson(Map<String, dynamic> json) => Place(
    store_name: json["store_name"],
    naver_category: json["naver_category"],
    address: json["address"],
    naver_map_url: json["naver_map_url"],
    main_img_url: json["main_img_url"],
    price_list: json["price_list"],
    open_time_list: json["open_time_list"],
    level_list: json["level_list"],
    change_time_list: json["change_time_list"],
  );
}

class PlaceList {
  final List<Place>? places;
  PlaceList({this.places});

  factory PlaceList.fromJson(String jsonString) {
    List<dynamic> listFromJson = json.decode(jsonString);
    List<Place> places = <Place>[];

    places = listFromJson.map((place) => Place.fromJson(place)).toList();
    return PlaceList(places: places);
  }
}