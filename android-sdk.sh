yay -S android-sdk
sudo chown -R $(whoami):$(whoami) /opt/android-sdk
mkdir $HOME/.android
touch $HOME/.android/repositories.cfg
export PATH="$PATH:/opt/android-sdk/tools/bin"
sdkmanager "platforms;android-29"
sdkmanager "platform-tools"
sdkmanager "build-tools;29.0.3"
sdkmanager --licenses

echo "Installed at /opt/android-sdk"
