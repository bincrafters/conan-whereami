# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class WhereamiConan(ConanFile):
    name = "whereami"
    version = "f3a86fdf17b49c434a16bb4d9e45a135d4cc25f9"
    description = "Locate the current executable and the current module/library on the file system"
    # topics can get used for searches, GitHub topics, Bintray tags etc. Add here keywords about the library
    topics = ("conan", "whereami", "c", "introspection", "getmodulefilename",
              "dladdr", "executable-path", "getexecutablepath")
    url = "https://github.com/bincrafters/conan-whereami"
    homepage = "https://github.com/gpakosz/whereami"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"  # Indicates license type of the packaged library; please use SPDX Identifiers https://spdx.org/licenses/
    exports = ["LICENSE.md"]      # Packages the license for the conanfile.py
    # Remove following lines if the target lib does not use cmake.
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    # Options may need to change depending on the packaged library.
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Custom attributes for Bincrafters recipe conventions
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def source(self):
        source_url = "https://github.com/gpakosz/whereami"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url,
                                                  self.version), sha256="53afc725fe2a2f733ea91c05373f8c51133f4904ae7c2771427c54099bf5c492")
        extracted_dir = self.name + "-" + self.version

        # Rename to "source_subfolder" is a convention to simplify later steps
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions['CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS'] = True
        cmake.configure(build_folder=self._build_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE.MIT", dst="licenses",
                  src=self._source_subfolder)
        include_folder = os.path.join(self._source_subfolder, "src")
        self.copy(pattern="*.h", dst="include", src=include_folder)
        self.copy(pattern="*.dll", dst="bin", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", keep_path=False)
        self.copy(pattern="*.a", dst="lib", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
