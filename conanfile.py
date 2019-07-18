# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class WhereamiConan(ConanFile):
    name = "whereami"
    version = "20190107"
    description = "Locate the current executable and the current module/library on the file system"
    topics = ("conan", "whereami", "introspection", "getmodulefilename",
              "dladdr", "executable-path", "getexecutablepath")
    url = "https://github.com/bincrafters/conan-whereami"
    homepage = "https://github.com/gpakosz/whereami"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    @property
    def _build_subfolder(self):
        return "build_subfolder"

    def configure(self):
        del self.settings.compiler.libcxx

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def source(self):
        sha256 = "53afc725fe2a2f733ea91c05373f8c51133f4904ae7c2771427c54099bf5c492"
        commit = "f3a86fdf17b49c434a16bb4d9e45a135d4cc25f9"
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, commit), sha256=sha256)
        extracted_dir = self.name + "-" + commit
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self._build_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE.*", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
