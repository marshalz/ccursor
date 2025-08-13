// swift-tools-version: 5.9
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "GinRummyTracker",
    platforms: [
        .iOS(.v17)
    ],
    products: [
        .library(
            name: "GinRummyTracker",
            targets: ["GinRummyTracker"]),
        .executable(
            name: "GinRummyTrackerApp",
            targets: ["GinRummyTrackerApp"]),
    ],
    dependencies: [
        // Dependencies go here
    ],
    targets: [
        .target(
            name: "GinRummyTracker",
            dependencies: []),
        .executableTarget(
            name: "GinRummyTrackerApp",
            dependencies: ["GinRummyTracker"]),
        .testTarget(
            name: "GinRummyTrackerTests",
            dependencies: ["GinRummyTracker"]),
    ]
)
