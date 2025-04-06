1. TODO IOS

1.1 https://stackoverflow.com/questions/76412148/what-is-the-new-option-enable-user-script-sandboxing-in-xcode-15

If it gives problems for your project, you can simply change ENABLE_USER_SCRIPT_SANDBOXING = YES back to NO in project.pbxproj if needed. In the Xcode GUI it is a boolean pick list or ASCII text (depending what you select for "open as".

npx expo run:ios --device

npx expo start