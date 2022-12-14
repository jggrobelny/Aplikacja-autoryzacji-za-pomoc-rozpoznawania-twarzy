# Install script for directory: C:/Users/jakub/Desktop/pythonProj/inz/cascades/data

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/out/install/x64-Debug (domyślnie)")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlibsx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/haarcascades/haarcascade_eye.xml;/haarcascades/haarcascade_eye_tree_eyeglasses.xml;/haarcascades/haarcascade_frontalcatface.xml;/haarcascades/haarcascade_frontalcatface_extended.xml;/haarcascades/haarcascade_frontalface_alt.xml;/haarcascades/haarcascade_frontalface_alt2.xml;/haarcascades/haarcascade_frontalface_alt_tree.xml;/haarcascades/haarcascade_frontalface_default.xml;/haarcascades/haarcascade_fullbody.xml;/haarcascades/haarcascade_lefteye_2splits.xml;/haarcascades/haarcascade_licence_plate_rus_16stages.xml;/haarcascades/haarcascade_lowerbody.xml;/haarcascades/haarcascade_profileface.xml;/haarcascades/haarcascade_righteye_2splits.xml;/haarcascades/haarcascade_russian_plate_number.xml;/haarcascades/haarcascade_smile.xml;/haarcascades/haarcascade_upperbody.xml")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/haarcascades" TYPE FILE FILES
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/haarcascades/haarcascade_eye.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/haarcascades/haarcascade_frontalcatface.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/haarcascades/haarcascade_frontalcatface_extended.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/haarcascades/haarcascade_frontalface_alt.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/haarcascades/haarcascade_frontalface_alt2.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/haarcascades/haarcascade_frontalface_alt_tree.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/haarcascades/haarcascade_frontalface_default.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/haarcascades/haarcascade_fullbody.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/haarcascades/haarcascade_lefteye_2splits.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/haarcascades/haarcascade_licence_plate_rus_16stages.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/haarcascades/haarcascade_lowerbody.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/haarcascades/haarcascade_profileface.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/haarcascades/haarcascade_righteye_2splits.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/haarcascades/haarcascade_russian_plate_number.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/haarcascades/haarcascade_smile.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/haarcascades/haarcascade_upperbody.xml"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlibsx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/lbpcascades/lbpcascade_frontalcatface.xml;/lbpcascades/lbpcascade_frontalface.xml;/lbpcascades/lbpcascade_frontalface_improved.xml;/lbpcascades/lbpcascade_profileface.xml;/lbpcascades/lbpcascade_silverware.xml")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/lbpcascades" TYPE FILE FILES
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/lbpcascades/lbpcascade_frontalcatface.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/lbpcascades/lbpcascade_frontalface.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/lbpcascades/lbpcascade_frontalface_improved.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/lbpcascades/lbpcascade_profileface.xml"
    "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/lbpcascades/lbpcascade_silverware.xml"
    )
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "C:/Users/jakub/Desktop/pythonProj/inz/cascades/data/out/build/x64-Debug (domyślnie)/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
