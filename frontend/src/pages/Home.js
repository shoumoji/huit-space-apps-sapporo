import React, { useCallback, useRef, useState, useEffect } from "react";
import { GoogleMap, useLoadScript } from "@react-google-maps/api";

// import mapStyles from "./mapUtils/mapStyles";
// 地図のデザインを指定することができます。
// デザインは https://snazzymaps.com からインポートすることができます。

const libraries = ["places"];
const mapContainerStyle = {
  height: `${window.innerHeight}px`,
  // width: `${window.innerWidth}px`,
  width: `100%`,
};
// 地図の大きさを指定します。

const options = {
  //   styles: mapStyles,
  disableDefaultUI: true,
  // デフォルトUI（衛星写真オプションなど）をキャンセルします。
  zoomControl: true,
};

const Home = () => {
  const [pins, setPins] = useState([]);
  const [load, setLoad] = useState(true);
  const { isLoaded, loadError } = useLoadScript({
    googleMapsApiKey: process.env.apiKey,
    libraries,
  });

  const mapRef = useRef();
  const onMapLoad = useCallback((map) => {
    mapRef.current = map;
  }, []);
  // API読み込み後に再レンダーを引き起こさないため、useStateを使わず、useRefとuseCallbackを使っています。

//   useEffect(() => {
//     if (isLoaded) {
//       getAllPosts().then((data) => {
//         setPins(data.data);
//         setLoad(false);
//       });
//     }
//   }, [isLoaded]);

  if (loadError) {
    alert("error while loading google map.");
    return <p>error while loading google map.: {loadError.toString()}</p>;
  }
  if (!isLoaded) return "Loading...";

  return (
    <GoogleMap
      className="GoogleMap"
      id="map"
      mapContainerStyle={mapContainerStyle}
      zoom={8} // デフォルトズーム倍率を指定します。
      center={{
        lat: 29.55208397599675,
        lng: -95.0980936737919,
      }} // 札幌周辺にデフォルトのセンターを指定しました。
      options={options}
      onLoad={onMapLoad}
    >
      {/* <PlaceInfo pins={pins} /> */}

    </GoogleMap>
  );
}

export default Home;