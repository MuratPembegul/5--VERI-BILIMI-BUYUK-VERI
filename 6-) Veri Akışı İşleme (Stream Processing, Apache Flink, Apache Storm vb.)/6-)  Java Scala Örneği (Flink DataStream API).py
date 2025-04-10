DataStream<String> stream = env.socketTextStream("localhost", 9999);
DataStream<Event> parsed = stream
    .map(line -> new Event(line))
    .assignTimestampsAndWatermarks(
        WatermarkStrategy
            .<Event>forMonotonousTimestamps()
            .withTimestampAssigner((event, timestamp) -> event.getTimestamp())
    );