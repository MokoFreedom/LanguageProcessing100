/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 1.3.40
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package org.chasen.cabocha;

public final class InputLayerType {
  public final static InputLayerType INPUT_RAW_SENTENCE = new InputLayerType("INPUT_RAW_SENTENCE");
  public final static InputLayerType INPUT_POS = new InputLayerType("INPUT_POS");
  public final static InputLayerType INPUT_CHUNK = new InputLayerType("INPUT_CHUNK");
  public final static InputLayerType INPUT_SELECTION = new InputLayerType("INPUT_SELECTION");
  public final static InputLayerType INPUT_DEP = new InputLayerType("INPUT_DEP");

  public final int swigValue() {
    return swigValue;
  }

  public String toString() {
    return swigName;
  }

  public static InputLayerType swigToEnum(int swigValue) {
    if (swigValue < swigValues.length && swigValue >= 0 && swigValues[swigValue].swigValue == swigValue)
      return swigValues[swigValue];
    for (int i = 0; i < swigValues.length; i++)
      if (swigValues[i].swigValue == swigValue)
        return swigValues[i];
    throw new IllegalArgumentException("No enum " + InputLayerType.class + " with value " + swigValue);
  }

  private InputLayerType(String swigName) {
    this.swigName = swigName;
    this.swigValue = swigNext++;
  }

  private InputLayerType(String swigName, int swigValue) {
    this.swigName = swigName;
    this.swigValue = swigValue;
    swigNext = swigValue+1;
  }

  private InputLayerType(String swigName, InputLayerType swigEnum) {
    this.swigName = swigName;
    this.swigValue = swigEnum.swigValue;
    swigNext = this.swigValue+1;
  }

  private static InputLayerType[] swigValues = { INPUT_RAW_SENTENCE, INPUT_POS, INPUT_CHUNK, INPUT_SELECTION, INPUT_DEP };
  private static int swigNext = 0;
  private final int swigValue;
  private final String swigName;
}

