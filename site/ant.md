# Ant

## Get all of the ant targets
`ant -p`

## Commenting out code with ifs (ant-contrib)
```ant
<if>
 <istrue value="false"/>
 <then>
    <!-- Stuff to comment out -->
 </then>
</if>

```
