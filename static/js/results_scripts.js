var jsonURL = "https://daemon-dash-galileo-rachitag22.c9users.io/return-result";

var dp = new DayPilot.Calendar("dp");

// behavior and appearance
dp.cssClassPrefix = "calendar_white";

// view
dp.startDate = "2014-02-24";
dp.days = 5;

dp.headerDateFormat = "dddd"; // day of week, long format (e.g. "Monday")

dp.events.list = [{
    "text":"CMSC131-0508 ",
    "end":"2014-02-24T16:50:00",
    "id":"0",
    "start":"2014-02-24T16:00:00",
    },
    
    {
    "text":"CMSC131-0508 ",
    "end":"2014-02-26T16:50:00",
    "id":"0",
    "start":"2014-02-26T16:00:00",
    },
    
    {
    "text":"CMSC131-0508 ",
    "end":"2014-02-28T16:50:00",
    "id":"0",
    "start":"2014-02-28T16:00:00",
    },
    
    {
    "text":"CMSC131-0508 Discussion",
    "end":"2014-02-24T15:50:00",
    "id":"3",
    "start":"2014-02-24T15:00:00",
    },
    
    {
    "text":"CMSC131-0508 Discussion",
    "end":"2014-02-26T15:50:00",
    "id":"3",
    "start":"2014-02-26T15:00:00",
    },
    
    {
    "text":"ASTR101-0108 ",
    "end":"2014-02-25T12:15:00",
    "id":"5",
    "start":"2014-02-25T11:00:00",
    },
    
    {
    "text":"ASTR101-0108 ",
    "end":"2014-02-27T12:15:00",
    "id":"5",
    "start":"2014-02-27T11:00:00",
    },
    
    {
    "text":"ASTR101-0108 Lab",
    "end":"2014-02-27T20:00:00",
    "id":"7",
    "start":"2014-02-27T18:00:00",
    },
    
    {
    "text":"ASTR101-0108 Discussion",
    "end":"2014-02-26T12:50:00",
    "id":"8",
    "start":"2014-02-26T12:00:00",
    },
    
    {
    "text":"CPSD100-0101 ",
    "end":"2014-02-27T17:20:00",
    "id":"9",
    "start":"2014-02-27T16:00:00",
    },
    
    {
    "text":"MATH241-0111 ",
    "end":"2014-02-24T09:50:00",
    "id":"10",
    "start":"2014-02-24T09:00:00",
    },
    
    {
    "text":"MATH241-0111 ",
    "end":"2014-02-26T09:50:00",
    "id":"10",
    "start":"2014-02-26T09:00:00",
    },
    
    {
    "text":"MATH241-0111 ",
    "end":"2014-02-28T09:50:00",
    "id":"10",
    "start":"2014-02-28T09:00:00",
    },
    
    {
    "text":"MATH241-0111 Discussion",
    "end":"2014-02-25T08:50:00",
    "id":"13",
    "start":"2014-02-25T08:00:00",
    },
    
    {
    "text":"MATH241-0111 Discussion",
    "end":"2014-02-27T08:50:00",
    "id":"13",
    "start":"2014-02-27T08:00:00",
    },
    
    {
    "text":"ENGL101S-0110 ",
    "end":"2014-02-24T09:50:00",
    "id":"15",
    "start":"2014-02-24T09:00:00",
    },
    
    {
    "text":"ENGL101S-0110 ",
    "end":"2014-02-26T09:50:00",
    "id":"15",
    "start":"2014-02-26T09:00:00",
    },
    
    {
    "text":"ENGL101S-0110 ",
    "end":"2014-02-28T09:50:00",
    "id":"15",
    "start":"2014-02-28T09:00:00",

    }];

$.get( "jsonURL", function( data ) {
    
dp.events.list = response;
alert("SLDKJKFLSKDFJSDLKFJ");
});

dp.init();
