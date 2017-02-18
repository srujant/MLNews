Cesium.BingMapsApi.defaultKey = "rAT6FD3QWEAHqFKTyVOH~PGug46gl7KWuYW5EmoKrhA~An9_0N3tOAo3VQ-1JgMBj3hOgSBb1-610evZpUQVW48gUc62JQ9RjNzRKSWBPLqI";
var viewer = new Cesium.Viewer('cesiumContainer');
  viewer.dataSources.add(Cesium.GeoJsonDataSource.load('Apps/SampleData/ne_10m_us_states.topojson', {
        stroke: Cesium.Color.BLACK,
        fill: Cesium.Color.BLUE.withAlpha(0.2),
        strokeWidth: 0
    }));
   var promise = Cesium.GeoJsonDataSource.load('Apps/SampleData/ne_10m_us_states.topojson');
    promise.then(function(dataSource) {
        viewer.dataSources.add(dataSource);

        //Get the array of entities
        var entities = dataSource.entities.values;
        
        var colorHash = {};
        for (var i = 0; i < entities.length; i++) {
            var entity = entities[i];
            var name = entity.name;
            //Replace population with number of tweets from state
            var population = entity.properties.Population;
            var color = colorHash[name];
            if (!color) {
                //Replace 38332521 with number of tweets that would make a state "hot"
                var alphalevel = population/38332521;
                color = Cesium.Color.RED.withAlpha(alphalevel);
                colorHash[name] = color;
            }
            
            entity.polygon.material = color;
            entity.polygon.outline = false;
        }
    }).otherwise(function(error){
        //Display any errrors encountered while loading.
        window.alert(error);
    });