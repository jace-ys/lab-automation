# `service.tecan-spark-relay`

The `service.tecan-spark-relay` is the service layer for interacting with a [Tecan Spark® Multimode Plate Reader](https://lifesciences.tecan.com/multimode-plate-reader) through the SparkControl API provided by Tecan. This API is not available publicly, so please contact your customer service representiative at Tecan to find out how you can access it.

## Supported APIs

- [`TecanSpark/v1alpha1`](#tecanspark/v1alpha1)

## Minimum Requirements

- SparkControl v3.1
- `.NET 5.0`
- A `bash`-like environment (eg. Git Bash, WSL2)

This service should run on the same Windows machine as the SparkControl software as it has to access the local SparkControl Automation Interface API.

## Usage

- Open the project in Visual Studio 2019 and follow the manual for setting up the SparkControl Automation Interface API.
- Build the solution in `Release` mode. This should place the `TecanSparkRelay` executable in the `./bin/Release` directory. You will need to tweak the post-build event for the project to copy the additional Automation Interface files to this same directory.

- Export the following environment variables to the current shell:

  ```
  export REDIS_PUBSUB_URL=<the URL for connecting to the pubsub.redis service>
  export MANAGER_DEVICE_NAME=<a unique name for the current device>
  export FORWARDER_DATA_GATEWAY_URL=<the base URL for the service.data-gateway>
  ```

  Other environment variables that can be configured can be found in [`Config.cs`](Config.cs).

- Run the server:

  ```
  ./bin/Release/TecanSparkRelay.exe run server
  ```

## How it Works

Upon receiving a protocol trigger, the `service.tecan-spark-relay` generates a corresponding method XML file that can be understood by the Spark®, based on the protocol's name and spec. For an example of how this XML file looks like, see the [method XML file template for the MeasureAbsorbance protocol](Methods/MeasureAbsorbance/Method.xml).

This method XML file is then passed to the SparkControl API to be executed. While the method is being executed, the `service.tecan-spark-relay` is blocked from handling new protocol triggers. You can view the method while it's being executed through the SparkControl Dashboard. If the Spark® stops running midway through, the execution will not complete successfully.

Once the method has completed execution, an XML file containing the measurement data produced by the Spark® is exported via the API. See [here for an example](Methods/MeasureAbsorbance/Export.xml) of this data export XML file. This file is then parsed and transformed into a format that can be pushed to the [`service.data-gateway`](../data-gateway).

## Protocols

#### `TecanSpark/v1alpha1`

Available protocols can be found under the [`Methods`](Methods) directory. Each protocol contains a README documenting the required `spec` to trigger it.

Examples of protocol triggers for the `service.tecan-spark-relay` can be found under [`protocols/examples/tecan-spark-relay`](../../protocols/examples/tecan-spark-relay).

## Data Export

The `service.tecan-spark-relay` forwards data produced by the Spark® to the `service.data-gateway` in the following format:

```json
{
  "timeElapsed": "time elapsed",
  "error": "error",
  "absorbance": "absorbance"
}
```

## Development

#### Mock SparkControl API

As the SparkControl API is only available on a machine with the SparkControl software installed, it might not always be very convenient when developing on another machine. To facilitate this, a mock implementation of the SparkControl API is provided for local development in the [`local` branch](https://github.com/jace-ys/lab-automation/tree/local/services/tecan-spark-relay).

#### Adding New Protocols

To implement new protocols that the `service.tecan-spark-relay` should handle, follow these steps:

- Create a new directory for your protocol under [`Methods`](Methods)
- Create a `Method.cs` file and write your implementation for the abstract class [`SparkMethod`](Methods/Registry.cs)
- Create a `Method.xml` file, containing a templated version of the method XML that your protocol should generate. One way to get started with this is to create a dummy version using the SparkControl Method Editor software, then use the `./bin/Release/TecanSpark.exe run export` utility to export it as an XML file. You can then edit this XML file accordingly such that it can be templated by your custom method in `Method.cs`.
- Add your method to the [`Registry`](Methods/Registry.cs)
